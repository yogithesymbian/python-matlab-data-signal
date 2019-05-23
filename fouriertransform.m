function [ X ] = ftransform(f,L1,L2 )

%   Detailed explanation goes here
% ftransform is a function which is use to convert time domin no preodic
% function  to frequency domin. It also draw the magnitude and Phase plot.
%syntax is given below..
%ftransform (function, first limit , final limit)


syms t
syms w j positive;

X= int(f*exp(-j*w*t),t,L1,L2);
%X=simplify(X);
disp(' X(jw)'),pretty(X)

w=-20:.01:20;
inline(X);  
ans(-20:.01:20);

subplot(2,1,1);
plot(w,real(ans),'g','linewidth',2)
title('|X(jw)| Frequency Domein ')
xlabel('(w)   Range')
grid on;

subplot(2,1,2)
plot(w,imag(ans),'r','linewidth',2.5);
title('< X(jw) Angle')
grid on 

 end

