// See https://aka.ms/new-console-template for more information
using System;
using Day_11;
List<Monkey> monkeys = new();

// I hardcoded input but ill parse it properly when ill have strength to do it
monkeys.Add(new Monkey(2, 3, 23, "old * 19", 79, 98)); // 0
monkeys.Add(new Monkey(2, 0, 19, "old + 6", 54, 65, 75, 74)); // 1
monkeys.Add(new Monkey(1, 3, 13, "old * old", 79, 60, 97)); //2
monkeys.Add(new Monkey(0, 1, 17, "old + 3", 74)); // 3

for(int i = 0; i < 20; i++)
{
    foreach(Monkey monkey in monkeys)
    {
        for(int j = 0; j < monkey.items.Count; j++)
        {
            monkey.InspectItem(j);
            monkey.ThrowItem(j, monkeys);
        }
        monkey.ClearHands();
    }
}

List<long> businesses = new();
foreach(Monkey monkey in monkeys)    
{
        Console.WriteLine(monkey.monkeyBusiness);
        businesses.Add(monkey.monkeyBusiness);
}
businesses.Sort();
businesses.Reverse();
Console.WriteLine(businesses[0]*businesses[1]);

// Part 2:
Console.WriteLine("-----------------");
monkeys.Clear();
monkeys.Add(new Monkey(6, 1, 5, "old * 2", 98, 89, 52));
monkeys.Add(new Monkey(2, 6, 2, "old * 13", 57, 95, 80, 92, 57, 78));
monkeys.Add(new Monkey(7, 5, 19, "old + 5", 82, 74, 97, 75, 51, 92, 83));
monkeys.Add(new Monkey(0, 4, 7, "old + 6", 97, 88, 51, 68, 76));
monkeys.Add(new Monkey(0, 1, 17, "old + 1", 63));
monkeys.Add(new Monkey(4, 3, 13, "old + 4", 94, 91, 51, 63));
monkeys.Add(new Monkey(2, 7, 3, "old + 2", 61, 54, 94, 71, 74, 68, 98, 83));
monkeys.Add(new Monkey(3, 5, 11, "old * old", 90, 56));
int maxValue = 5 * 2 * 19 * 7 * 17 * 13 * 3 * 11;

for (int i = 0; i < 10000; i++)
{
    foreach (Monkey monkey in monkeys)
    {
        for (int j = 0; j < monkey.items.Count; j++)
        {
            monkey.InspectItem2(j, maxValue);
            monkey.ThrowItem(j, monkeys);
        }
        monkey.ClearHands();
    }
}
foreach(var monkey in monkeys)
    Console.WriteLine(monkey.monkeyBusiness);
businesses.Clear();
foreach (Monkey monkey in monkeys)
{
    Console.WriteLine(monkey.monkeyBusiness);
    businesses.Add(monkey.monkeyBusiness);
}
businesses.Sort();
businesses.Reverse();
Console.WriteLine(businesses[0] * businesses[1]);

