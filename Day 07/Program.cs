using System.Text.RegularExpressions;

using Day_07;

var input = File.ReadAllText("commands.txt");
var commands = input.Split('\n');

Regex cdRegex = new Regex(@"\$ cd (\w+|\.\.|\/)");
Regex lsRegex = new Regex(@"\$ ls");
Regex fileRegex = new Regex(@"(\d+) ([\w\.]+)");
Regex dirRegex = new Regex(@"dir (\w+)");


Folder root = new Folder();
List<Folder> folders = new();

folders.Add(root);
Folder currentFolder = root;

foreach (var command in commands)
{
    var cdMatch = cdRegex.Match(command);
    if (cdMatch.Success)
    {
        string name = cdMatch.Groups[1].ToString();
        if (name == @"/")
            currentFolder = root;
        else if (name == "..")
            currentFolder = currentFolder.parent;
        else
        {
            foreach(var component in currentFolder.components)
            {
                if (component is Folder d)
                {
                    if (d.name == name)
                    {
                        currentFolder = d;
                    }
                }
            }
        }
    }
    var lsMatch = lsRegex.Match(command);
    if (lsMatch.Success)
    {
        // :+1:
    }
    var fileMatch = fileRegex.Match(command);
    if (fileMatch.Success)
    {
        int size = int.Parse(fileMatch.Groups[1].ToString());
        string name = fileMatch.Groups[2].ToString();
        FolderFile ffile = new(currentFolder, size, name);
        currentFolder.components.Add(ffile);
    }
    var dirMatch = dirRegex.Match(command);
    if (dirMatch.Success)
    {
        string name = dirMatch.Groups[1].ToString();
        Folder folder = new(currentFolder, name);
        currentFolder.components.Add(folder);
        folders.Add(folder);
    }

    
}
int answer = 0;
int freeSpace = 70000000 - root.GetSize();
int neededSpace = 30000000 - freeSpace;
List<int> sizes = new();
foreach (var folder in folders)
{ 
    int size = folder.GetSize();
    sizes.Add(size);
    if(size <= 100_000)
        answer += size;
}
Console.WriteLine($"part 1: {answer}");

sizes.Sort();
foreach(var size in sizes)
{
    if(size >= neededSpace)
    {
        Console.WriteLine($"Part 2: {size}");
        break;
    }
}