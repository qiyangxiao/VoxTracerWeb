import React from 'react';
import { Flex, Layout, Typography } from 'antd';
import LoginForm from '../components/LoginForm';
import { headerStyle, contentStyle } from '../style';
import { HomeHeader } from '../components/HomeItem';
import { handleLogin } from '../router';

const { Header, Content } = Layout; // 布局
const { Title } = Typography; // 文字排版

export default function Login() {
    return (
        <>
            <Layout>
                <Header style={headerStyle}>
                    <HomeHeader/>
                </Header>
                <Content style={contentStyle}>
                <Title>Welcome to VoxTracer</Title>
                    <Flex
                        justify='center'
                        align='center'
                    >
                        <LoginForm
                            handleLogin={handleLogin}
                        />
                    </Flex>
                </Content>
            </Layout>
        </>
    );
}
