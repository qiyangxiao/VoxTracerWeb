import *  as Utils from './utils';

// 处理登录表单
export const handleLogin = async (formData) => {
    const form = new FormData();
    for (const key in formData) {
        if (formData.hasOwnProperty(key)) {
            form.append(key, formData[key]);
        }
    }
        
    try {
        const response = await fetch('/handlelogin', {
            method: 'POST',
            body: form,
        });
        const data = await response.json();

        if (response.ok) {
            if (data.ok === 1) {
                Utils.openMessage(data.message, 'success');
                Utils.redirectTo('/', 3000);
            }
            else {
                Utils.openNotification('登录失败', data.message, 'error');
            }
        }
    }
    catch (error) {
        Utils.openNotification('ERROR', 'Something went wrong...', 'error');
    }

}

// 处理注册表单
export const handleRegister = async(formData) => {
    console.log('Received values: ', formData);
    const form = new FormData();
    for (const key in formData) {
        if (formData.hasOwnProperty(key)) {
            form.append(key, formData[key]);
        }
    }

    try {
        const response = await fetch('/handleregister', {
            method: 'POST',
            body: form,
        });
        const data = await response.json();

        if (response.ok) {
            if (data.ok === 1) {
                Utils.openMessage(data.message, 'success');
            }
            else {
                Utils.openNotification('注册失败', data.message, 'error');
            }
        }
    }
    catch (error) {
        Utils.openNotification('ERROR', 'Something went wrong...', 'error');
    }
};


// 检查登录状态
export const checkLoginStatus = async(setIsLoggedIn, setUserId) => {
    try {
        const response = await fetch('/checkloggedin', {
            method: 'POST',
            body: JSON.stringify({'': ''})
        });
        const data = await response.json();
        console.log(data);
        if (response.ok) {
            if ( data.ok === 1) {
                setUserId(data.uid);
                setIsLoggedIn(true);
            }
            else {
                setUserId(null);
                setIsLoggedIn(false);
            }
        } 

    }
    catch(error) {
        setIsLoggedIn(false);
    }
};

// 处理登出状态
export const handleLogout = async(setIsLoggedIn, setUserId) => {
    try {
        const response = await fetch('/handlelogout', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({'': ''}),
        });
        const data = await response.json();

        if (response.ok) {
            if (data.ok === 1) {
                setIsLoggedIn(false);
                setUserId('');
                Utils.openMessage(data.message, 'success');
            }
            else {
                Utils.openNotification('登出失败', data.message, 'error');
            }
        }
    }
    catch (error) {
        Utils.openNotification('ERROR', 'Something went wrong...', 'error');
    }
};

// 处理上传文件
export const dragUpload = {
    name: 'audio_input',
    multiple: false,
    action: '/upload',
    onChange(info) {
      const { status, response } = info.file;
      if (status !== 'uploading') {
        console.log(info.file, info.fileList);
      }
      if (status === 'done') {
        if (response.ok === 1) {
            Utils.openMessage(`${info.file.name} file uploaded successfully.`, 'success');
        }
        else {
            Utils.openMessage(`${info.file.name}：${response.message}`, 'error');
        }

      } else if (status === 'error') {
        Utils.openMessage(`${info.file.name} file upload failed.`, 'error');
      }
    },
    onDrop(e) {
      console.log('Dropped files', e.dataTransfer.files);
    },
};

// 处理发送验证码
export const handleSendCaptcha = async(email) => {
    try {
        const response = await fetch('/sendcode', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({'email': email}),
        });
        const data = await response.json();

        if (response.ok) {
            if (data.ok === 1) {
                Utils.openMessage(data.message, 'success');
            }
            else {
                Utils.openNotification('验证码发送失败', data.message, 'error');
            }
        }
    }
    catch (error) {
        Utils.openNotification('ERROR', 'Something went wrong...', 'error');
    }
};