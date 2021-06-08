#include<stdio.h>
#include<stdlib.h>
#define ElemType int
#define MaxL 100
#define Error 0
#define OK 1
typedef int status;

typedef struct node{
    ElemType element;
    struct node *link;
}node;
typedef struct {
    struct node *first;
    int n;
}singlelist;
status Init (singlelist *L){
    L->first=NULL;
    L->n=0;
	return OK; 
}
status Input(singlelist *L){
	int n;
	int i;
	 printf("input the number of elements:");
	 scanf("%d",&n);
	 L->n=n;
	 L->first=(node *)malloc(sizeof(node));
	 node *p=L->first;
	 for (i=0;i<n-1;i++){
		scanf("%d",&(p->element));
		p->link=(node *)malloc(sizeof(node));
		p=p->link;
	 }
	scanf("%d",&(p->element));
	p->link=NULL; 	
	return OK;
}

status output(singlelist L){
	if(L.first==NULL) return Error;
	node *p=L.first;
	do{
		printf("%d " , (p->element));
		p=p->link;
	}while(p->link!=NULL);
	printf("%d \n",p->element );
	return OK;
}

status reserve(singlelist *L){
	if(L->first==NULL) return Error;
	node *p=L->first;
	node *q=NULL;
	node *temp;
 	while(p->link){
 		temp=p->link;
 		p->link=q;
 		q=p;
 		p=temp;
	 }
	 p->link=q;
	 L->first=p;
	 return OK;	
}
void check(status x){
     if(x!=OK){
     	printf("Oops,Error code:%d\n",x);
     	exit(1);
	 }
	 else return ;
}
int main(){
	singlelist L;
	status pres;
	pres= Init(&L);
	check(pres);
	pres=Input(&L);
	check(pres);
	pres=reserve(&L);
	check(pres);
	printf("reversed:\n");
	pres=output(L);
	check(pres);
	return 0;
}
