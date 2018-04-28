function b = valid_position(x, y, m, n)
	if (x < 1 || x > m || y < 1 || y > n)
		b = 0;
	else
		b = 1;
	end
end
