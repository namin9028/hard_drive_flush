function [ploc rloc tloc] = ecg(amp, rloc, t)
%normalize data
norm_amp = (amp - min(amp)) / (max(amp) - min(amp));
pvec = [];
tvec = [];
a = [];
b = [];
for x = 1:length(rloc)
   for y = t(rloc(x))-0.25:t(rloc(x))
       pvec = [pvec norm_amp(y)];
       p = max(pvec);
       y = y + 0.001; %revise number depending on sampling frequency
   end
   for z = t(rloc(x)):t(rloc(x))+0.5
       tvec = [tvec norm_amp(z)];
       tt = max(tvec);
       z = z + 0.001; %revise number depending on sampling frequency
   end     
    a = [a p];
    b = [b tt];
    x = x + 1;
end
ploc = a;
tloc = b;
end
%Deal with edges