function v = shift_variation(img, x, y, lenW, dx, dy)

	[m,n] = size(img);
	mo = m-(floor(lenW/2)*2);
	no = n-(floor(lenW/2)*2);
	b = valid_position(x+dx, y+dy, mo, no);
	
	if (b)
		x = x+floor(lenW/2);
		y = y+floor(lenW/2);
		subO = img(x-floor(lenW/2):x+floor(lenW/2), y-floor(lenW/2):y+floor(lenW/2));
		x = x+dx;
		y = y+dy;
		subM = img(x-floor(lenW/2):x+floor(lenW/2), y-floor(lenW/2):y+floor(lenW/2));
		v = sum(sum((subM-subO).^2));
	else
		v = 0;
	end

end
