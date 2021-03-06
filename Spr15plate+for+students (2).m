function out = Spr15plate
    % this is a .m file for numerically integrating a simplified form of the
    % N-S equations for a moving plate using the semi-infinite approximation
    % Notation: n is eta, a is a vector containing the functions g and f
    % Students must replace ************ with suitable values/expressions
    ni = 0; % first integration point for eta
    nf = 3; % final integration point for eta
    step = 0.01; % interval for numerical solution of ode system
    dn = step;
    nspan = ni:dn:nf;
    options=odeset('AbsTol',1E-10,'RelTol',1E-4,'maxstep',step); % specify ode solution parameters
   
    
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Defining initial Conditions 
    % Defining the array, a0, that will house initial conditions
        a0 = zeros(2,1); 
        a0(1) = ************; % specify g(0) 
        a0(2) = ************; % specify f(0) 
        % integration
        [n,a]=ode45(@plate,nspan,a0,options);
        out = [n,a];
        plot(n,a);
        legend('df/dn','f');
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        % description of derivatives

            function dadn=plate(n, b)
                           
                 dadn= b;  % setting up vector containing derivatives

                 dadn(1) = *************; %  specify dg/dn
                 dadn(2) = *************; %  specify df/dn
                       
            end
       
end
           
        
       