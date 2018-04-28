function [corners, corner_map] = corner_detection_moravec(img, threshold, lenW, filename)

	[m,n] = size(img);
	img_copy = zeros(m+(floor(lenW/2)*2), n+(floor(lenW/2)*2));
	img_copy(floor(lenW/2)+1:m+floor(lenW/2), floor(lenW/2)+1:n+floor(lenW/2)) = img;

	corner_map = zeros(m,n);	
	
	%shift variation
	for i=1:m
		for j=1:n

			v = zeros(1,8);
			v(1) = shift_variation(img_copy, i, j, lenW, 0, 1);
			v(2) = shift_variation(img_copy, i, j, lenW, 1, 0);
			v(3) = shift_variation(img_copy, i, j, lenW, 0, -1);
			v(4) = shift_variation(img_copy, i, j, lenW, -1, 0);
			v(5) = shift_variation(img_copy, i, j, lenW, 1, 1);
			v(6) = shift_variation(img_copy, i, j, lenW, -1, -1);	
			v(7) = shift_variation(img_copy, i, j, lenW, 1, -1);
			v(8) = shift_variation(img_copy, i, j, lenW, -1, 1);
			corner_map(i,j) = min(v);

		end
	end

	%threshold
	for i=1:m
		for j=1:n
			if corner_map(i,j) < threshold		
				corner_map(i,j) = 0;
			end
		end
	end

	%non-maximal suppression
	corner_map_copy = zeros(m+(floor(lenW/2)*2), n+(floor(lenW/2)*2));
	corner_map_copy(floor(lenW/2)+1:m+floor(lenW/2), floor(lenW/2)+1:n+floor(lenW/2)) = corner_map;
	for i=1:m
		for j=1:n
				corner_map(i,j) = non_maximal_suppression(corner_map_copy, i, j, lenW);
		end
	end
	imwrite(corner_map,'corner_map.png');

	hold on;
	imshow(img);
	%draw corners;
	for i=1:m
		for j=1:n
				if (corner_map(i,j)!= 0)
						h = plot(j,i,'r','markersize', 7);				
				end
		end
	end
	saveas (h, filename);
end
