import React from "react";
import remarkGfm from "remark-gfm";
import ReactMarkdown from "react-markdown";
import { useParams } from "react-router-dom";

const markdown = `A paragraph with *emphasis* and **strong importance**.

> A block quote with ~strikethrough~ and a URL: https://reactjs.org.

* Lists
* [ ] todo
* [x] done

A table:

Ký hiệu  | Giải thích
------------- | -------------
C  | Mạng CNN cơ bản(dim: 32, kerner: 3x3, pading: 1, stride: 1)
R  | Mạng RNN cơ bản( h0 size(2,batchsize,1024/2)
"+"| cộng 2 mạng 
"-"| nối 2 mạng
`

const BlogDetail = () => {
  const { blogid } = useParams();
  return (
    <div className="p-4">
      {blogid}
      <ReactMarkdown children={markdown} remarkPlugins={[remarkGfm]} />
    </div>
  );
};

export default BlogDetail;
