#include <string>
using namespace std;


bool isSubstring(string str1, string str2){
	//Using Sunday Algorithm
	size_t length_1 = str1.length(), length_2 = str2.length();
	if (length_2 > length_1) return false;
	size_t i = 0;
	while (i <= (length_1 - length_2)){
		size_t compared = 0;
		for (size_t j = i; j < length_1; j++){
			if (str1[j] != str2[j - i]){
				size_t change_to = i + length_2;
				while (change_to < length_1 && str2.find_first_of(str1[change_to]) == string::npos){ change_to += length_2; }
				if (change_to > length_1  || str2.find_first_of(str1[change_to]) == string::npos) return false;
				else{ i = change_to - str2.find_first_of(str1[change_to]); break; }
			}
			else{
				if (++compared == length_2) return true;
				continue;
			}
		}
	}
	return false;
}
