import React from "react";
import { LockOutlined, UserOutlined } from '@ant-design/icons';
import { Button, Form, Input, Flex } from 'antd';
import { openMessage } from "../utils";

export default function LoginForm({ handleLogin }) {
    const [form] = Form.useForm();

    return(

        <Form
            form={form}
            onFinish={handleLogin}
            name="login"
            className="login-form"
        >
            <Form.Item
                name="uid"
                rules={[
                    {
                        required: true,
                        message: '请输入你的邮箱或用户ID！',
                    }
                ]}
            >
                <Input 
                    prefix={<UserOutlined className="site-form-item-icon" />} 
                    placeholder="邮箱或用户ID..."
                />
            </Form.Item>
            <Form.Item
                name="pwd"
                rules={[
                    {
                        required: true,
                        message: '请输入你的密码！',
                    }
                ]}
            >
                <Input.Password
                    prefix={<LockOutlined className="site-form-item-icon" />}
                    type="password"
                    placeholder="密码..."
                />
            </Form.Item>
            <Form.Item 
                name="href"                 
            >
                <Flex
                    justify="space-between"
                    align="center"
                >
                    <a href="/onregister">马上注册！</a>
                    <a 
                        className="login-form-forgot" 
                        href="#"
                        onClick={() => openMessage('请联系管理员重置密码！', 'error')}
                    >
                        忘记密码？
                    </a>
                </Flex>

            </Form.Item>

            <Form.Item>
                <Button
                    type="primary"
                    size="large"
                    htmlType="submit"
                    className="login-form-button"
                >
                     登录
                </Button>
            </Form.Item>

        </Form>
    );
}
