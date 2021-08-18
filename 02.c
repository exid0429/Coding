#include <stdio.h>
int main(void)
{
    int i=0;
    int sum = 0;
    int num, tmp;

    printf("정수는 총 몇개인가요? :");
    scanf("%d",&num);

    while(i<num) {
        printf("No.%d : ", i+1);
        scanf("%d", &tmp);
        sum += tmp;
    }

    printf("총합 : %d\n", sum);
    printf("평균값 : %.2f\n", (double)sum/num);

}