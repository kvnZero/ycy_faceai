var app = new Vue({
    el: '#app',
    data: {
        show2: false,
        show: false,
        userinfo: "登录",
        userinfoBot: "注册",
        userif: "没",
        infoIcon: false,
        // input的绑定值
        ruleForm2: {
            name: "",
            pass: "",
            checkPass: "",
            age: ""
        }
    },
    methods: {
        submitForm(formName) {
            // let that = this;
            // this.$refs[formName].validate(valid => {
            if (valid) {
                that.show = false;
                that.userinfo = "登录";
                that.userif = "没";
                that.userinfoBot = "注册";
                that.infoIcon = false;
                // console.log(value);
            } else {
                // console.log("error submit!!");
                return false;
            }
            // });
        },
        Landing(formName) {
            let that = this;
            //重置表单数据
            // this.$refs[formName].resetFields();
            if (that.show) {
                that.show = false;
                that.userinfo = "登录";
                that.userif = "没";
                that.userinfoBot = "注册";
                that.infoIcon = false;
            } else {
                that.show = true;
                that.userinfo = "注册";
                that.userif = "已";
                that.userinfoBot = "登录";
                that.infoIcon = true;
            }
        }
        // resetForm(formName) {
        //   this.$refs[formName].resetFields();
        // }
    }
})
// 搜索框
var app = new Vue({
    el: '#skr',
    data: {
        input2: ''
    }
})