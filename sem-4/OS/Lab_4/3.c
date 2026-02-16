main()
{
    int a = 10;
    if (fork() == 0)
        a++;
    printf("%d\n", a);
}

