import {
  FileOutlined,
  TeamOutlined,
  UserOutlined,
  HomeOutlined,
} from "@ant-design/icons";
import { Outlet } from "react-router-dom";
import Bee from "../pages/Bee";
import Blog from "../pages/Blog";
import BlogDetail from "../pages/BlogDetail";
import Home from "../pages/Home";
import Tom from "../pages/Tom";
import User from "../pages/User";

export const BASE_ROUTER = [
  {
    label: "BlogDetail",
    key: "blogDetail",
    path: "blog/:blogid",
    element: <BlogDetail />,
  },
];

export const PUBLIC_ROUTER = [
  {
    label: "Home",
    key: "home",
    icon: <HomeOutlined />,
    children: null,
    path: "home",
    element: <Home />,
  },
  {
    label: "User",
    key: "user",
    icon: <UserOutlined />,
    children: [
      {
        label: "Tom",
        key: "tom",
        icon: null,
        children: null,
        path: "tom",
        element: <Tom />,
      },
      {
        key: "bill",
        label: "Bill",
        path: "bill",
      },
    ],
    path: "user",
    element: <Outlet />,
  },
  {
    label: "Team",
    key: "team",
    icon: <TeamOutlined />,
    children: [
      {
        key: "team1",
        label: "Team1",
        path: "team1",
      },
      {
        key: "team2",
        label: "Team2",
        path: "team2",
      },
    ],
    path: "team",
  },
  {
    label: "BLog",
    key: "blog",
    icon: <FileOutlined />,
    children: null,
    path: "blog",
    element: <Blog />,
  },
  {
    label: "Bee",
    key: "bee",
    icon: <FileOutlined />,
    children: null,
    path: "bee",
    element: <Bee />,
  },
];
