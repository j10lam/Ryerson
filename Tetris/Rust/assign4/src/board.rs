use super::block;

#[derive(Clone, Default)]
pub struct Board {
    pub c: usize,
    pub r: usize,
    pub rows: Vec<Vec<char>>,
}

// new(): creates a new instance of Board and returns it
pub fn new(num_cols: usize, num_rows: usize) -> Board {
    Board {
        c: num_cols,
        r: num_rows,
        rows: create_rows(num_cols, num_rows)
    }
}

// create_row(): creates a vector of rows to represent the game board
pub fn create_rows(c: usize, mut r: usize) -> Vec<Vec<char>> {
    let mut rows: Vec<Vec<char>> = vec![];

    while r > 0 {
        rows.push(vec![' '; c]);
        r -= 1;
    }

    return rows
}

impl Board {

    //add_block(): adds each square in the frozen list onto the board
    pub fn add_block(&mut self, t: block::Frozen) {
        for sq in t.list.iter() {
            self.rows[sq.r as usize][sq.c as usize] = sq.l;
        }
    }

    //add_powerup(): adds each powerup onto the board
    pub fn add_powerup(&mut self, power_up: Vec<block::Powerup>) {
        for p in power_up.iter() {
            self.rows[p.r][p.c] = 'x';
        }
    }

    //format_board(): formats the board and returns it
    pub fn format_board(&mut self, count: i32) -> Vec<String> {
        let mut output: Vec<String> = Vec::new();

        for row in self.rows.iter() {
            let mut row_str: String = row.iter().collect();
            row_str.push('|');
            row_str.insert(0, '|');
            output.push(row_str);
        }

        let s = match count as u32 {
            1 => " piece",
            _ => " pieces"
        };

        let mut last = output.pop().unwrap();
        last.push(' '); last.push_str(&count.to_string()); last.push_str(s);
        output.push(last);

        output.reverse();

        let mut bottom = vec!['-'; self.c];
        bottom.push('+'); bottom.insert(0, '+');
        output.push(bottom.iter().collect());

        return output
    }
}
