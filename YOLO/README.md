# traffic 데이터를 활용한 영상 인식

## 목표
>  [직진, (비보호)좌회전, 우회전] 가능한 상황인지 판단해서 Boolean List로 반환

>  e.g.) [True, False, True]

## 교차로 로드뷰로 사진 데이터를 수집해서 Label
- 차량 신호등 (traffic_light1)
- 차량 초록불 (green_light1)
- 차량 빨간불 (red_light2)
- 좌회전불 (left_light)
- 비보호좌회전 (left_sign)
- 횡단보도 신호등 (traffic_light2)
- 횡단보도 초록불 (green_light2)
- 횡단보도 빨간불 (red_light2)

![traffic](https://user-images.githubusercontent.com/113752736/206138737-66bbb9d6-d5f6-426b-b683-e95d852d56e1.png)
