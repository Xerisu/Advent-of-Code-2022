using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Day_07
{
    internal class Folder : IComponent
    {
        public Folder parent;
        public List<IComponent> components;
        public string name;

        public Folder(Folder parent, string name)
        {
            this.parent = parent;
            this.name = name;
            components = new List<IComponent>();

        }

        public Folder()
        {
            this.parent = this;
            this.components = new();
            this.name = "root";
        }

        public int GetSize()
        {
            int size = 0;
            foreach(var component in components)
            {
                size += component.GetSize();
            }
            return size;
        }
    }
    internal class FolderFile : IComponent
    {
        public Folder parent;
        public int size;
        public string name;

        public FolderFile(Folder parent, int size, string name)
        {
            this.parent = parent;
            this.size = size;
            this.name = name;
        }
        public int GetSize()
        {
            return size;
        }
    }
}
