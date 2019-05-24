%% Z transform
clc
close all % close all
clear all % clear all variable
x = [ 1 5 0 3 9 9 ];
b = 0;
% calculating length of an birth of date
n = length(x);
y = sym('z');
for i = 1:n
    b = b+x(i)*y^(1-i);
end
display(b);
% reference at https://youtu.be/lpBhat9mVho