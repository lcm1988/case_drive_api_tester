#coding:utf-8
from tools.data_compare import datacompare

a={"status":"200","data":{"userId":7480717,"is_login":True,"unpayedNum":0,"unreceivedNum":21,"favoriteNum":7,"cartNum":13,"couponNum":49,"amount":"421.00","uncommentNum":0,"refundNum":0,"topicNum":1,"followNum":0,"fansNum":0,"favoriteTopicNum":0,"commentTopicNum":0,"userLevel":"\u8fbe\u4ee4\u5e2e\u5802\u4e3b","userLevelImgUrl":"http:\/\/img.beta.daling.com\/zin\/2015\/10\/13\/00FADB1NU1BD64SHG.png","concernUserQuantity":0,"concernTagQuantity":0,"userDesc":"\u8fd9\u4e2a\u4eba\u6709\u70b9\u61d2,\u6682\u65f6\u8fd8\u6ca1\u6709\u4ecb\u7ecd\u54e6~","userLevelUrl":"http:\/\/touch.daling.com\/dal_l.html?req_user_id=7480717&user_id=7480717","subjectSectionNum":30,"favoritesMyQuantity":0,"favoritesMyNewQuantity":0,"commentMyQuantity":0,"commentMyNewQuantity":0,"newFansQuantity":0,"newTopQuantity":0,"newRecommendQuantity":0,"topQuantity":0,"recommendQuantity":0,"notifyTotalNumber":0,"duobao_url":"","act_id":"0","receive_words":"","coupon_type":"activity","has_wait_comment":"0","has_admin_reply":"0","comment_txt":"","my_coin":85501,"my_xp":440,"my_level_image":"http:\/\/img1.cdn.daling.com\/st\/zt\/images\/coin_images\/Medal_2.png","my_level_name":"\u4e2d\u7ea7\u8fbe\u4ee4","my_coin_url":"http:\/\/m.ymall.com\/pages\/web_member_center\/coin-list\/coin-list.html","my_xp_url":"http:\/\/m.ymall.com\/api\/topics\/details?tid=812947","my_level_url":"http:\/\/m.ymall.com\/pages\/web_member_center\/member_level\/member_level.html","my_xp_detail_url":"http:\/\/m.ymall.com\/pages\/web_member_center\/member_level\/lntimacy_details.html","sign_in_url":"http:\/\/m.ymall.com\/pages\/web_member_center\/sign_in\/sign_in.html","coupon_exchange_url":"http:\/\/m.ymall.com\/pages\/web_member_center\/coupon_exchange\/coupon_exchange.html","user_center_url":"http:\/\/m.ymall.com\/pages\/web_member_center\/member_center\/member_center.html"}}
b={"status":"200","data":{"userId":15015054,"is_login":True,"unpayedNum":2,"unreceivedNum":26,"favoriteNum":3,"cartNum":3,"couponNum":1,"amount":"999999.00","uncommentNum":0,"refundNum":0,"topicNum":0,"followNum":0,"fansNum":0,"favoriteTopicNum":0,"commentTopicNum":0,"userLevel":"\u666e\u901a\u7528\u6237","userLevelImgUrl":"","concernUserQuantity":0,"concernTagQuantity":0,"userDesc":"\u8fd9\u4e2a\u4eba\u6709\u70b9\u61d2,\u6682\u65f6\u8fd8\u6ca1\u6709\u4ecb\u7ecd\u54e6~","userLevelUrl":"http:\/\/touch.daling.com\/dal_l.html?req_user_id=15015054&user_id=15015054","subjectSectionNum":1,"favoritesMyQuantity":0,"favoritesMyNewQuantity":0,"commentMyQuantity":0,"commentMyNewQuantity":0,"newFansQuantity":0,"newTopQuantity":0,"newRecommendQuantity":0,"topQuantity":0,"recommendQuantity":0,"notifyTotalNumber":0,"duobao_url":"","act_id":"247","receive_words":"\u9886\u53d6429\u5143\u7ea2\u5305","has_wait_comment":"0","has_admin_reply":"0","comment_txt":"","my_coin":1000000,"my_xp":143,"my_level_image":"http:\/\/img1.cdn.daling.com\/st\/zt\/images\/coin_images\/Medal_2.png","my_level_name":"\u4e2d\u7ea7\u8fbe\u4ee4","my_coin_url":"http:\/\/m.ymall.com\/pages\/web_member_center\/coin-list\/coin-list.html","my_xp_url":"http:\/\/m.ymall.com\/api\/topics\/details?tid=812947","my_level_url":"http:\/\/m.ymall.com\/pages\/web_member_center\/member_level\/member_level.html","my_xp_detail_url":"http:\/\/m.ymall.com\/pages\/web_member_center\/member_level\/lntimacy_details.html","sign_in_url":"http:\/\/m.ymall.com\/pages\/web_member_center\/sign_in\/sign_in.html","coupon_exchange_url":"http:\/\/m.ymall.com\/pages\/web_member_center\/coupon_exchange\/coupon_exchange.html","user_center_url":"http:\/\/m.ymall.com\/pages\/web_member_center\/member_center\/member_center.html"}}
l=datacompare(b,a,'/')
for i in l:
    print i