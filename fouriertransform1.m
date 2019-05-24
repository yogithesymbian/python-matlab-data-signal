// syms t v w x;
// x from birth of my date
// f = exp(-x^2);
// fw=fourier(f);

syms t w;
x = -exp(-t)*heaviside(t)+3*dirac(t);
fw = fourier(x)

// use pretty(fw) | for test the fourier