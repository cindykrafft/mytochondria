function buf = read_24bit(filename, offset, numwords)
% Pure-MATLAB/Octave replacement for FieldTrip's read_24bit MEX:
% read NUMWORDS little-endian signed 24-bit integers starting at byte OFFSET.
fid = fopen(filename, 'rb', 'ieee-le');
if fid < 0, error('read_24bit: cannot open %s', filename); end
fseek(fid, offset, 'bof');
b = fread(fid, [3, numwords], 'uint8=>double');
fclose(fid);
buf = b(1,:) + 256*b(2,:) + 65536*b(3,:);
buf(buf >= 2^23) = buf(buf >= 2^23) - 2^24;
buf = buf(:);
end
