extern crate assign4;
use assign4::board;
use assign4::dice;
use assign4::block;

use std::io::{self, Read};
//use std::fmt;

#[derive(Default)]
pub struct Game {
    board: board::Board,
    dice: dice::Dice,
    current_block: block::Tetromino,
    frozens: block::Frozen,
    powerups: Vec<block::Powerup>,
    count: i32,
    game_over: bool,
}

impl std::fmt::Display for Game {

    //fmt() formats the Game instance
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        let rows = self.board.clone().format_board(self.count);
        let mut board_string = "".to_string();
        for row in rows {
            board_string.push_str(&row);
            board_string.push('\n');
        }

        write!(f, "{}", board_string)
    }
}

impl Game {

    //new() creates and returns a new instance of Game
    fn new() -> Game {
        Game{
            board: board::new(0,0),
            dice: dice::new(),
            current_block: block::new(),
            frozens: block::new_frozen(),
            ..Default::default()
        }
    }

    //check_collisions() checks if there are any block-block collisions
    fn check_collisions(&mut self, actual_block: Vec<block::Square>) -> bool {
        let mut hit = false;
        for p in actual_block.iter() {
            if !(hit) {
                hit = self.frozens.list.iter().any(|pt| pt.c == p.c && pt.r == p.r);
            }
        }
        return hit
    }

    //powerup_collisions() checks if current block has overlapped a powerup
    fn powerup_collisions(&mut self) -> i32 {
        let mut count = 0;
        let mut hit;
        let block = self.current_block.get_block();
        for p in block {
            hit = self.powerups.iter().any(|pt| pt.c as i32 == p.c && pt.r as i32 == p.r);
            if hit {count += 1;}
        }
        return count
    }

    //check_bounds() checks to see if the block will be out of bounds after a proposed
    //               move
    fn check_bounds(&mut self, actual_block: Vec<block::Square>) -> bool {
        let oob;
        let c = self.board.c as i32 - 1;
        let r = self.board.r as i32 - 1;

        oob = actual_block.iter()
        .any(|pt| pt.r < 0 || pt.r > r || pt.c < 0 || pt.c > c);

        return oob
    }

    //moves() reads in a command and moves the current block
    fn moves(&mut self, command: &str) {

        let mut future_block = self.current_block.clone();
        let letter = future_block.pivot.l;

        match command {
            "l" => future_block.translate((-1,0)),
            "r" => future_block.translate((1,0)),
            "L" => {if letter != 'y' {future_block.rotate_left()}},
            "R" => {if letter != 'y' {future_block.rotate_right()}},
            "." => future_block.down(),
            "+" => {self.current_block.falling = true;
                    while self.current_block.falling {self.moves(".");}
                    },
            _ => ()
        };

        if command != "+" {
            if self.check_collisions(future_block.get_block())
            || self.check_bounds(future_block.get_block()) {
                if command == "." {
                    self.current_block.set_frozen();
                    self.frozens.add_frozen(self.current_block.get_block());
                    self.frozens.clear_line(self.board.c as i32, self.board.r as i32);
                    self.new_block();
                }
            } else {
                self.current_block = future_block;
                let mut num = self.powerup_collisions();

                while num > 0 && command == "." && !self.current_block.falling {
                    self.frozens.pwrup_clear(self.board.c as i32, self.board.r as i32);
                    num -=1;
                }
            }
        }
    }

    //new_block() creates a new block and replces current_block
    fn new_block(&mut self) {
        self.current_block = block::new();
        self.current_block.create_block(self.dice.roll(), self.dice.roll());
        self.current_block.spawn_block(self.board.c as f32, self.board.r as i32);


        let block = self.current_block.clone().get_block();
        if self.check_collisions(block) {
            self.game_over = true;
        } else {
            self.count += 1;
        }
    }

}

//read_from() reads in a string and begins the game
pub fn read_from(buffer: &str) -> Game {
    let mut commands: Vec<&str> = buffer.split_terminator(|c| c == '\n' || c == '\r').collect();
    commands.retain(|ref s| !s.is_empty());

    let mut g = Game::new();

    for command in commands.iter() {
        let mut command_vec: Vec<&str> = command.split(' ').collect();
        let first = command_vec.remove(0);


        let mut numbers: Vec<&str> = command_vec.clone();
        numbers.retain(|ref _s| first != "moves");
        let c: Vec<usize> = numbers.clone().into_iter().map(|s| s.to_string().parse::<usize>().unwrap()).collect();

        match first {
            "board" => g.board = board::new(c[0], c[1]),
            "dice" => {
                g.dice = dice::Dice{i: 0, seq: c};
                g.new_block();
            },
            "powerup" => g.powerups.push(block::new_powerup(c[0]-1, c[1]-1)),
            "moves" => {
                for mvs in command_vec {
                    let mut m: Vec<&str> = mvs.split_terminator("").collect();
                    m.retain(|&c| c != "");

                    for letter in m {
                        if !g.game_over {g.moves(letter);}
                    }
                }
            },
            _ => g.game_over = true
        };
    }

    if !g.game_over {
        g.frozens.add_frozen(g.current_block.get_block());
    }

    g.board.add_powerup(g.powerups.clone());
    g.board.add_block(g.frozens.clone());
    return g;
}

//format_game() formats the Game instance and returns a String
pub fn format_game(g: Game) -> String {
    g.to_string()
}


//main() the main function of this module
fn main() {
    let mut buffer = String::new();
    let stdin = io::stdin();
    let mut handle = stdin.lock();

    handle.read_to_string(&mut buffer).unwrap();

    let g: Game = read_from(&buffer);

    print!("{}", g);
}

mod test;
