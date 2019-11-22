extern crate num_bigint;

use std::thread;


use num_traits::Pow;
use num_bigint::BigUint;

fn exec(me: u8, a: u32, b:u32, shift: u32) {
    let exponent: u32 = 100000000;
    let two = "2".parse::<BigUint>().unwrap();
    let mut num = Pow::pow(&two, exponent);
    let mut step=0;
    for exponent in (a+shift..b).step_by(2) {
        step+=1;
        if step==250 {
            println!("{}: {}\t\t{}", me, exponent-a-shift, exponent-a);
            step=0;
        }

        num = &num * &two;
        if &num % 100000000u32 == BigUint::from(exponent as u32) {
            println!("Solution: 2^{}", exponent);
            panic!();
        }
    }
}

fn main() {
    let shift = 551500;
    let ds=3392500+1630000;
    let child1 = thread::spawn(move || {exec(1, 100000000, 212500000, shift+ds);});
    let child2 = thread::spawn(move || {exec(2, 212500000, 325000000, ds);});
    let child3 = thread::spawn(move || {exec(3, 325000000, 437500000, shift+ds);});
    let child4 = thread::spawn(move || {exec(4, 437500000, 550000000, ds);});
    let child5 = thread::spawn(move || {exec(5, 550000000, 662500000, shift+ds);});
    let child6 = thread::spawn(move || {exec(6, 662500000, 775000000, ds);});
    let child7 = thread::spawn(move || {exec(7, 775000000, 887500000, shift+ds);});
    let child8 = thread::spawn(move || {exec(8, 887500000, 999999999, ds);});
    child1.join();
    child2.join();
    child3.join();
    child4.join();
    child5.join();
    child6.join();
    child7.join();
    child8.join();
}

