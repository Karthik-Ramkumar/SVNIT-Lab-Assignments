#include <stdio.h>

int main()
{
    int numberOfSegments;
    int segmentNumber, offset;
    int i;

    printf("Enter number of segments: ");
    scanf("%d", &numberOfSegments);

    int segmentBase[numberOfSegments];
    int segmentLimit[numberOfSegments];

    printf("Enter base and limit for each segment:\n");
    for (i = 0; i < numberOfSegments; i++)
    {
        printf("Segment %d Base: ", i);
        scanf("%d", &segmentBase[i]);

        printf("Segment %d Limit: ", i);
        scanf("%d", &segmentLimit[i]);
    }

    printf("\nStatic Segment Table:\n");
    printf("Segment\tBase\tLimit\n");
    for (i = 0; i < numberOfSegments; i++)
    {
        printf("%d\t%d\t%d\n", i, segmentBase[i], segmentLimit[i]);
    }

    printf("\nEnter logical address (segment number and offset): ");
    scanf("%d %d", &segmentNumber, &offset);

    if (segmentNumber < 0 || segmentNumber >= numberOfSegments)
    {
        printf("Invalid segment number\n");
    }
    else if (offset < 0 || offset >= segmentLimit[segmentNumber])
    {
        printf("Segmentation Fault: Offset exceeds segment limit\n");
    }
    else
    {
        int physicalAddress = segmentBase[segmentNumber] + offset;
        printf("Physical Address = %d\n", physicalAddress);
    }

    return 0;
}