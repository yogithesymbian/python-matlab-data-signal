% yogi arif widodo
% 17 615 006
% x(n) =  { 1 5 0 3 9 9}
% konvolusi dari y(n)
n=0:5;
x=1.5.^n;
hn=0:40;
h=1.2.^hn;
y=conv(x,h);
batas=0:80;
figure, subplot(3,1,1);
grid on;
stem(n,x), subplot(3,1,2);
stem(hn,h), subplot(3,1,3);
stem(batas,y);