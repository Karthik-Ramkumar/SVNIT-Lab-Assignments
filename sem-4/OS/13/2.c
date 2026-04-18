#include <stdio.h>

int main()
{
    int totalSegments;
    int i;
    int segmentNumber, offset;

    printf("Enter number of segments: ");
    scanf("%d", &totalSegments);

    int base[totalSegments];
    int limit[totalSegments];

    printf("Enter base address and limit for each segment:\n");
    for (i = 0; i < totalSegments; i++)
    {
        printf("Segment %d Base: ", i);
        scanf("%d", &base[i]);

        printf("Segment %d Limit: ", i);
        scanf("%d", &limit[i]);
    }

    printf("\nSegment Table:\n");
    printf("Segment No.\tBase\tLimit\n");
    for (i = 0; i < totalSegments; i++)
    {
        printf("%d\t\t%d\t%d\n", i, base[i], limit[i]);
    }

    printf("\nEnter logical address (segment number and offset): ");
    scanf("%d %d", &segmentNumber, &offset);

    if (segmentNumber < 0 || segmentNumber >= totalSegments)
    {
        printf("Invalid segment number\n");
    }
    else if (offset < 0 || offset >= limit[segmentNumber])
    {
        printf("Segmentation Fault! Offset exceeds segment limit\n");
    }
    else
    {
        int physicalAddress = base[segmentNumber] + offset;
        printf("Physical Address = %d\n", physicalAddress);
    }

    return 0;
}