use std::ops::Neg;

#[derive(Clone, Default)]
pub struct Square {
    pub c: i32,
    pub r: i32,
    pub l: char
}

#[derive(Clone, Default)]
pub struct Tetromino {
    pub pivot: Square,
    pub squares: Vec<Square>,
    pub is_frozen: bool,
    pub falling: bool
}

#[derive(Clone)]
pub struct Powerup {
    pub c: usize,
    pub r: usize,
}

#[derive(Clone, Default)]
pub struct Frozen {
    pub list: Vec<Square>
}

//new_sq() creates and returns a new Square instance
pub fn new_sq() -> Square {
    Square {..Default::default()}
}

//new() creates and returns a new Tetromino instance
pub fn new() -> Tetromino {
    Tetromino {
        pivot: new_sq(),
        ..Default::default()
    }
}

//new_powerup() creates and returns a new Powerup instance
pub fn new_powerup(c: usize, r: usize) -> Powerup {
    Powerup{c,r}
}

//new_frozen() creates and returns a new Frozen instance
pub fn new_frozen() -> Frozen {
    Frozen {..Default::default()}
}

//database() returns the appropriate tetris piece and a default pivot of type Square
pub fn database(t: i32) -> (Vec<Square>, Square) {
    let letters: [char; 7] = ['y','r','g','b','o','p','c'];
    let l = letters[(t-1) as usize];
    let pivot = Square {c: 0, r: 0, l};

    let squares = match t {
        1 => vec![Square{c:0,r:0,l}, Square{c:1,r:0,l}, Square{c:0,r:1,l}, Square{c:1,r:1,l}],
        2 => vec![Square{c:0,r:0,l}, Square{c:-1,r:1,l}, Square{c:1,r:0,l}, Square{c:0,r:1,l}],
        3 => vec![Square{c:0,r:0,l}, Square{c:-1,r:0,l}, Square{c:0,r:1,l}, Square{c:1,r:1,l}],
        4 => vec![Square{c:0,r:0,l}, Square{c:-1,r:0,l}, Square{c:1,r:0,l}, Square{c:-1,r:1,l}],
        5 => vec![Square{c:0,r:0,l}, Square{c:-1,r:0,l}, Square{c:1,r:0,l}, Square{c:1,r:1,l}],
        6 => vec![Square{c:0,r:0,l}, Square{c:-1,r:0,l}, Square{c:1,r:0,l}, Square{c:0,r:1,l}],
        7 => vec![Square{c:0,r:0,l}, Square{c:-1,r:0,l}, Square{c:1,r:0,l}, Square{c:2,r:0,l}],
        _ => vec![Square{c:0,r:0, l:' '}],
    };

    return (squares, pivot);
}

impl Tetromino {

    //create_block() creates a new tetris block
    pub fn create_block(&mut self, t: i32, r: i32) {
        let (squares, pivot) = database(t);
        self.pivot = pivot;
        self.squares = squares;

        if self.pivot.l != 'y' {
            for _n in 0..(r-1) {
                self.rotate_right();
            }
        }
    }

    //spawn_block() puts tetris piece in appropriate location on the board
    pub fn spawn_block(&mut self, c: f32, r: i32) {
        let mid = (c / 2.0).round() - 1.0;
        let offset = r - self.find_max() - 1;

        self.pivot.c = mid as i32;
        self.pivot.r = offset;
    }

    //get_block() returns the actual coordinates of the tetris block
    pub fn get_block(&mut self) -> Vec<Square> {
        let mut actual = self.squares.clone();

        for sq in &mut actual {
            sq.c += self.pivot.c;
            sq.r += self.pivot.r;
        }

        return actual
    }

    //find_max() returns the maximum row number
    pub fn find_max(&mut self) -> i32 {
        let mut max = 0;
        for sq in self.squares.iter() {
            if max < sq.r {
                max = sq.r
            }
        }
        return max;
    }

    //set_frozen() sets the block to frozen
    pub fn set_frozen(&mut self) {
        self.is_frozen = true;
    }

    //rotate_left() rotates the block left
    pub fn rotate_left(&mut self) {
        let mut temp = Vec::new();
        for sq in self.squares.iter() {
            temp.push(sq.rotate_left_sq());
        }
        self.squares = temp;
    }

    //rotate_right() rotates the block right
    pub fn rotate_right(&mut self) {
        let mut temp = Vec::new();
        for sq in self.squares.iter() {
            temp.push(sq.rotate_right_sq());
        }
        self.squares = temp;
    }

    //translate() translates the block horizontally given a coordinate
    pub fn translate(&mut self, o: (i32,i32)) {
        self.pivot.c += o.0;
        self.pivot.r += o.1;
    }

    //down() moves the block down 1 row
    pub fn down(&mut self) {
        self.pivot.r -=1;
    }

}

impl Frozen {

    //add_frozen() adds the current block to the list of frozen blocks
    pub fn add_frozen(&mut self, mut t: Vec<Square>) {
        self.list.append(&mut t);
    }

    //clear_line() clears all full lines
    pub fn clear_line(&mut self, cols: i32, rows: i32) {
        let mut full_row = self.find_rows(cols, rows);

        while full_row != -1 {
            self.list.retain(|ref sq| sq.r != full_row);
            self.shift(full_row);
            full_row = self.find_rows(cols, rows);
        }
    }

    //pwrup_clear() clears the last row with one less than max number of cols
    pub fn pwrup_clear(&mut self, cols: i32, rows: i32) {
        let row = self.find_rows(cols-1, rows);
        if row != -1 {
            self.list.retain(|ref sq| sq.r != row);
            self.shift(row);;
        }
    }

    //find_row() finds and returns a list of rows for which meets the target
    pub fn find_rows(&mut self, target: i32, rows: i32) -> i32 {
        let mut found_row = -1;
        for r in 0..(rows-1) {
            let mut num: Vec<Square> = self.list.clone();
            num.retain(|ref sq| sq.r == r);
            if num.len() == target as usize {found_row = r; break;}
        }
        return found_row;
    }

    //shift() shifts all frozen blocks down 1 if their row is greater than the param
    pub fn shift(&mut self, row: i32) {
        for sq in &mut self.list {
            if sq.r > row {
                sq.down();
            }
        }
    }
}

impl Square {

    //rotate_left_sq() rotates the square left
    pub fn rotate_left_sq(&self) -> Square {
        Square {c: self.r.neg(), r: self.c, l: self.l}
    }

    //rotate_right_sq() rotates the square right
    pub fn rotate_right_sq(&self) -> Square {
        Square {c: self.r, r: self.c.neg(), l: self.l}
    }

    //down() moves the square down one row
    pub fn down(&mut self) {
        self.r -= 1;
    }
}
