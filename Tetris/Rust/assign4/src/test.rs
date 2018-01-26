#[cfg(test)]
use super::read_from;
#[allow(unused_imports)]
use super::format_game;
#[test]
fn tiny_empty_board() {
    assert_eq!(
        "|       | 0 pieces\n\
         |       |\n\
         |       |\n\
         |       |\n\
         +-------+\n",
        format_game(read_from( "board 7 4")))}

#[test]
fn larger_empty_board() {
    assert_eq!(
        "|        | 0 pieces\n\
         |        |\n\
         |        |\n\
         |        |\n\
         |        |\n\
         |        |\n\
         +--------+\n",
        format_game(read_from( "board 8 6")))}

#[test]
fn odd_size_board_with_powerups() {
    assert_eq!(
        "|       | 0 pieces\n\
         |  x    |\n\
         |       |\n\
         | x     |\n\
         +-------+\n",
        format_game(read_from( "board 7 4\n\
                                powerup 3 3\n\
                                powerup 2 1")))}

//  testSimpleEvenWidth
#[test]
fn podium() {
    assert_eq!(
        "|   p    | 1 piece\n\
         |  ppp   |\n\
         |        |\n\
         |        |\n\
         |        |\n\
         |        |\n\
         +--------+\n",
        format_game(read_from( "board 8 6\n\
                                dice 6 1\n\
                                moves")))}

#[test]
fn podium_rotated() {
    assert_eq!(
        "|   p    | 1 piece\n\
         |   pp   |\n\
         |   p    |\n\
         |        |\n\
         |        |\n\
         |        |\n\
         +--------+\n",
        format_game(read_from( "board 8 6\n\
                                dice 6 2\n\
                                moves")))}

#[test]
fn green_piece() {
    assert_eq!(
        "|   gg   | 1 piece\n\
         |  gg    |\n\
         |        |\n\
         |        |\n\
         |        |\n\
         |        |\n\
         +--------+\n",
        format_game(read_from( "board 8 6\n\
                                dice 3 1\n\
                                moves")))}

#[test]
fn green_rotated() {
    assert_eq!(
        "|   g    | 1 piece\n\
         |   gg   |\n\
         |    g   |\n\
         |        |\n\
         |        |\n\
         |        |\n\
         +--------+\n",
        format_game(read_from( "board 8 6\n\
                                dice 3 2\n\
                                moves ")))}

#[test]
fn upside_w() {
    assert_eq!(
        "|   gg   | 1 piece\n\
         |  gg    |\n\
         |        |\n\
         |        |\n\
         |        |\n\
         |        |\n\
         +--------+\n\
         ",
        format_game(read_from( "board 8 6\n\
                                dice 3 3\n\
                                moves R")))}

#[test]
fn green_can_rotate() {
    assert_eq!(
        "|   g    | 1 piece\n\
         |   gg   |\n\
         |    g   |\n\
         |        |\n\
         |        |\n\
         |        |\n\
         +--------+\n",
        format_game(read_from( "board 8 6\n\
                                dice 3 1\n\
                                moves R")))}

#[test]
fn two_pieces() {
    assert_eq!(
        "|   c    | 2 pieces\n\
         |   c    |\n\
         |   c    |\n\
         |   c    |\n\
         |        |\n\
         |        |\n\
         |        |\n\
         |        |\n\
         |   yy   |\n\
         |   yy   |\n\
         +--------+\n",
        format_game(read_from( "board 8 10\n\
                                dice 1 2 7 2 2\n\
                                moves +")))}

#[test]
fn cyan_unrotated() {
    assert_eq!(
        "|  cccc  | 2 pieces\n\
         |        |\n\
         |        |\n\
         |        |\n\
         |        |\n\
         |        |\n\
         |        |\n\
         |        |\n\
         |   yy   |\n\
         |   yy   |\n\
         +--------+\n",
        format_game(read_from( "board 8 10\n\
                                dice 1 1 7 1 2\n\
                                moves +")))}

#[test]
fn three_pieces() {
    assert_eq!(
        "|  rr    | 3 pieces\n\
         |   rr   |\n\
         |        |\n\
         |        |\n\
         |   c    |\n\
         |   c    |\n\
         |   c    |\n\
         |   c    |\n\
         |   yy   |\n\
         |   yy   |\n\
         +--------+\n",
        format_game(read_from( "board 8 10\n\
                                dice 1 2 7 2 2\n\
                                moves ++")))}

#[test]
fn two_pieces_with_powerup() {
    assert_eq!(
        "|        | 2 pieces\n\
         | x      |\n\
         |   c    |\n\
         |   c    |\n\
         |   c    |\n\
         |   c    |\n\
         |        |\n\
         |        |\n\
         |yy      |\n\
         |yy      |\n\
         +--------+\n",
        format_game(read_from( "board 8 10\n\
                                powerup 2 9\n\
                                dice 1 2 7 2 2\n\
                                moves ll ll\n\
                                moves +..")))}

#[test]
fn two_pieces_with_powerup_hidden() {
    assert_eq!(
        "|        | 2 pieces\n\
         | c      |\n\
         | c      |\n\
         | c      |\n\
         | c      |\n\
         |        |\n\
         |        |\n\
         |        |\n\
         |yy      |\n\
         |yy      |\n\
         +--------+\n",
        format_game(read_from( "board 8 10\n\
                                powerup 2 9\n\
                                dice 1 2 7 2 2\n\
                                moves ll ll\n\
                                moves +ll.")))}


//  testSimpleOddWidth
#[test]
fn odd_green() {
    assert_eq!(
        "|   gg  | 1 piece\n\
         |  gg   |\n\
         |       |\n\
         |       |\n\
         |       |\n\
         |       |\n\
         +-------+\n",
        format_game(read_from( "board 7 6\n\
                                dice 3 1\n\
                                moves")))}

#[test]
fn odd_green_rotated() {
    assert_eq!(
        "|   g   | 1 piece\n\
         |   gg  |\n\
         |    g  |\n\
         |       |\n\
         |       |\n\
         |       |\n\
         +-------+\n",
        format_game(read_from( "board 7 6\n\
                                dice 3 2\n\
                                moves ")))}

#[test]
fn odd_2_pieces() {
    assert_eq!(
        "|   c   | 2 pieces\n\
         |   c   |\n\
         |   c   |\n\
         |   c   |\n\
         |       |\n\
         |       |\n\
         |       |\n\
         |       |\n\
         |   yy  |\n\
         |   yy  |\n\
         +-------+\n",
        format_game(read_from( "board 7 10\n\
                                dice 1 2 7 2 2\n\
                                moves +")))}

#[test]
fn odd_2_cyan_horizontal() {
    assert_eq!(
        "|  cccc | 2 pieces\n\
         |       |\n\
         |       |\n\
         |       |\n\
         |       |\n\
         |       |\n\
         |       |\n\
         |       |\n\
         |   yy  |\n\
         |   yy  |\n\
         +-------+\n",
        format_game(read_from( "board 7 10\n\
                                dice 1 1 7 1 2\n\
                                moves +")))}

#[test]
fn odd_3_pieces() {
    assert_eq!(
        "|  rr   | 3 pieces\n\
         |   rr  |\n\
         |       |\n\
         |       |\n\
         |   c   |\n\
         |   c   |\n\
         |   c   |\n\
         |   c   |\n\
         |   yy  |\n\
         |   yy  |\n\
         +-------+\n",
        format_game(read_from( "board 7 10\n\
                                dice 1 2 7 2 2\n\
                                moves ++")))}


//  testMultipiece
#[test]
fn four_pieces() {
    assert_eq!(
        "|   gg  | 4 pieces\n\
         |  gg   |\n\
         |   c   |\n\
         |   c   |\n\
         |   c   |\n\
         |   c   |\n\
         |  rr   |\n\
         |   rr  |\n\
         |   gg  |\n\
         |  gg   |\n\
         +-------+\n",
        format_game(read_from( "board 7 10\n\
                                dice 3 1 2 1 7 2\n\
                                moves +++++++++++")))}

#[test]
fn twenty_pieces() {
    assert_eq!(
        "|        | 20 pieces\n\
         |        |\n\
         |   c    |\n\
         |   c    |\n\
         |   c    |\n\
         |   c    |\n\
         |   c    |\n\
         |   c    |\n\
         |   c    |\n\
         |   c    |\n\
         +--------+\n",
        format_game(read_from( "board 8 10\n\
                                dice 7 2\n\
                                moves r+ rr+ rrr+ rrrr+ l+ ll+ lll+ Rrrrrr+ rrrr+ rrrr+ rrrr+ rrrr+ + Rllll+ lll+ ll+ l+  +++++++")))}

#[test]
fn fourteen_pieces() {
    assert_eq!(
        "|   c    | 14 pieces\n\
         |   c    |\n\
         |   c    |\n\
         |  xc    |\n\
         |   c    |\n\
         |   c    |\n\
         |   c    |\n\
         |cccc    |\n\
         |cccc    |\n\
         |cccc    |\n\
         +--------+\n",
        format_game(read_from( "board 8 10\n\
                                dice 7 2\n\
                                powerup 3 7\n\
                                moves r+ rr+ rrr+ rrrr+ l+ ll+ lll+ l....r +Rrrrr+lll+ll+l++++")))}
