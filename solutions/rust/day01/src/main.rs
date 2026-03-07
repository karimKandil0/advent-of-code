use std::colletion:HashMap;
use std::fs;

fn parse(input: &str) -> i64 {
  let left = Vec::new();
  let right = Vec::new();

  for line in input.lines() {
      let parts: Vec<&str> = line.split(": ").collect();
      let a = parts[0].parse::<i32>().expect("Failed to parse");
      let b = parts[1].parse::<i32>().expect("Failed to parse");
      left.push(a);
      right.push(b);
  }

  (left, right)

}

fn part1(input: &str) -> i64 {
    let (mut left, mut right) = parse(input);

    left.sort();
    right.sort();

    left.iter()
        .zip(right.iter())
        .map(|(a, b)| (a - b).abs())
        .sum()
}

fn part2(input: &str) -> i64 {
    let  (left, right) = parse(input);

    let mut counts = HashMap::new();
    for &num in &right {
        *counts.entry(num).or_insert(0) += 1;
    }

    left.iter()
        .map(|x| x * counts.get(x).unwrap_or(&0))
        .sum()


}

fn main() {
    let input = fs::read_to_string("../../../inputs/day01.txt")
        .expect("Failed to read input");

    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}
