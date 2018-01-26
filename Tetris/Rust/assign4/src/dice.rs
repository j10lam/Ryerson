#[derive(Default)]
pub struct Dice
{
    pub i: usize,
    pub seq: Vec<usize>,
}

//new() creates and returns a new Dice instance
pub fn new() -> Dice {
    Dice {..Default::default()}
}

impl Dice {

    //roll() rolls the dice and returns result
    pub fn roll(&mut self) -> i32 {
        let curr = self.seq[self.i];
        self.i += 1;

        if self.i >= self.seq.len(){
            self.i = 0;
        }

        return curr as i32
    }
}
