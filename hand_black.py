#黑名单
def hand_black(func):
    def wapper(*args,**kwargs):
        from page.base_page import BasePage
        instance:BasePage=args[0]
        try:
            return func(*args,**kwargs)
        except Exception as e:
            if instance.error_num>instance.max_num:
                raise e
            instance.error_num=+1
            for black_ele in instance.black_list:
                ele=instance.driver.find_elements(*black_ele)
                if len(ele)>0:
                    ele[0].click()
                    return func(*args,**kwargs)
                raise e
    return wapper