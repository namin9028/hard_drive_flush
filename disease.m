function out = disease(plocations)
%plocations has to be a column vector
x = diff(plocations);
a = [];
for y = 1:length(x)
    %Sinus arrhythmia ecg criteria is that PP interval should be at least
    %0.12s. 
    if x(y) > 0.12
        a = [a 1];
    else 
        a = [a 0];
    end
    y = y + 1;
end
%Vector a checks if any PP distance is greater than 0.12s. This is used to
%see if the person has the disease or not. 
if any(a) == 1
    out = 'Sorry bud';
else
    out = 'You live, this time';
end
end
