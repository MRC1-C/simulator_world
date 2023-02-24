import React, { useEffect, useState } from "react";

const Test = () => {
  const [t, setT] = useState(0);
  console.log(1)
  useEffect(() => {
    setT(1);
    setT(2)
  }, []);
  return <div>{t}</div>;
};

export default Test;
