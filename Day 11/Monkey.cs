using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Day_11
{
    internal class Monkey
    {
        public List<long> items;
        private string[] _operation;
        private long _divisionTest;
        private int[] _throwToMonkey = new int[2];

        public long monkeyBusiness;

        public Monkey(int monkeyTrue, int monkeyFalse, long divisibleTest, string operation, params long[] items)
        {
            _throwToMonkey[0] = monkeyTrue;
            _throwToMonkey[1] = monkeyFalse;
            _divisionTest = divisibleTest;
            _operation = operation.Split(' ');
            this.items = items.ToList();

            monkeyBusiness = 0;
        }

        public void InspectItem(int index)
        {
            long left = 0;
            if (!long.TryParse(_operation[0], out left))
                left = items[index];

            long right = 0;
            if (!long.TryParse(_operation[2], out right))
                right = items[index];

            if (_operation[1] == "*")
                items[index] = (left * right) / 3;
            if (_operation[1] == "+")
                items[index] = (left + right) / 3;

            monkeyBusiness++;
        }

        public void InspectItem2(int index, long maxValue)
        {
            if (!long.TryParse(_operation[0], out long left))
                left = items[index];

            if (!long.TryParse(_operation[2], out long right))
                right = items[index];

            if (_operation[1] == "*")
                items[index] = (left * right) % maxValue;
            if (_operation[1] == "+")
                items[index] = (left + right) % maxValue;

            monkeyBusiness++;
        }

        public void ThrowItem(int index, List<Monkey> monkeys)
        {
            Debug.Assert(items[index] > 0);
            if (items[index] % _divisionTest == 0)
                monkeys[_throwToMonkey[0]].items.Add(items[index]);
            else
                monkeys[_throwToMonkey[1]].items.Add(items[index]);
        }
        public void ClearHands()
        {
            items.Clear();
        }
    }
}
