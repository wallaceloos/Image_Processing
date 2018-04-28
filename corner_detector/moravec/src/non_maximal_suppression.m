function r = non_maximal_suppression(corner_map, x, y, lenW)

	x = x+floor(lenW/2);
	y = y+floor(lenW/2);
	subO = corner_map(x-floor(lenW/2):x+floor(lenW/2), y-floor(lenW/2):y+floor(lenW/2));

	cont = 0;	
	[m,n] = size(subO);
	for i=1:m
		for j=1:n	
			if (corner_map(x,y) >= subO(i,j))
				cont = cont+1;
			end
		end
	end

	if (cont < (m*n))
		r = 0;
	else
		r = corner_map(x,y);
	end

end
