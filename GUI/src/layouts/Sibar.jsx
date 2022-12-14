import React, { useState } from "react";
import { Image, Layout, Menu } from "antd";
import { PUBLIC_ROUTER } from "../router";
import { useLocation, useNavigate } from "react-router-dom";
import "./Sibar.css";
const { Sider } = Layout;

const Sibar = () => {
  const { pathname } = useLocation();
  const navigate = useNavigate();
  const [keys, setKeys] = useState(pathname.split("/").reverse().slice(0, -1));
  return (
    <Sider theme="light">
      <div
        className="logo"
        style={{
          padding: 16,
          display: "flex",
          flexDirection: "row",
          alignItems: "center",
          justifyContent: "center",
          width: "100%",
        }}
      >
        <Image
          src="/logo.png"
          width={40}
          height={40}
          style={{ cursor: "pointer" }}
          preview={false}
          onClick={() => navigate("home")}
        />
        <p
          style={{
            color: "black",
            fontWeight: 700,
            fontSize: 24,
            paddingLeft: 10,
          }}
        >
          CJ
        </p>
      </div>
      <Menu
        theme="light"
        selectedKeys={keys}
        mode="inline"
        items={PUBLIC_ROUTER}
        onClick={(e) => {
          navigate(e.keyPath.reverse().join("/"));
          setKeys(e.keyPath.reverse());
        }}
      ></Menu>
    </Sider>
  );
};

export default Sibar;
