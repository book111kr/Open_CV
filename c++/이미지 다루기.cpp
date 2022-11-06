#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>

//#include <opencv2/opencv.hpp>

#include <iostream>

using namespace cv;
using namespace std;

int main()
{
	Mat image;
	image = imread("house.jpg", IMREAD_COLOR); // IMREAD_COLOR, IMREAD_UNCHANGED,
	if (image.empty())                         // IMREAD_GRAYSCALE
	{
		cout << "Could not open or find the image" << endl;
		return -1;
	}

	namedWindow("Original", WINDOW_AUTOSIZE);  //WINDOW_AUTOSIZE : 윈도우 크기에 맞춰 이미지 불러옴
						   //WINDOW_NORMAL : 이미지를 사용자가 직접 조정 가능
	//namedWindow("Original", WND_PROP_FULLSCREEN);
	//SetWindowProperty("Original", WND_PROP_FULLSCREEN, WINDOW_FULLSCREEN); : 전체화면으로 불러옴
	imshow("Original", image);                 //트랙바를 붙이는 경우를 제외하고 named함수 생략가능

	waitkey(0);

	return 0;
}
