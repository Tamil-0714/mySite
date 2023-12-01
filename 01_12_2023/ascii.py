ch =65
while ch<123:
	if ch in range(91,96):
		continue
	print(f"ASCII value {ch} ASCII char {chr(ch)}")
	ch += 1