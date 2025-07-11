string a = Console.ReadLine();
string b = Console.ReadLine();

int num = int.Parse(a);
char[] arr = b.ToCharArray();

int res1 = num * (arr[2] - '0');
int res2 = num * (arr[1] - '0');
int res3 = num * (arr[0] - '0');

Console.WriteLine(res1);
Console.WriteLine(res2);
Console.WriteLine(res3);
Console.WriteLine(res1 + res2 * 10 + res3 * 100);