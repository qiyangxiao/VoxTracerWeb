import React from 'react';
import { Flex, Layout, Typography } from 'antd';
import RegisterForm from '../components/RegisterForm';
import { handleRegister } from '../router';
import { headerStyle, contentStyle } from '../style';
import { HomeHeader } from '../components/HomeItem';


const { Header, Content } = Layout; // 布局
const { Title } = Typography; // 文字排版

export default function Register() {

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
                        <RegisterForm
                            handleRegister={handleRegister}
                        />
                    </Flex>
                </Content>
            </Layout>
        </>
    );
}
