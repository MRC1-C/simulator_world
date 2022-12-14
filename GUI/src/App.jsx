import BaseLayout from "./layouts/BaseLayout";
import { Routes, Route } from "react-router-dom";
import NotFound from "./layouts/NotFound";
import { BASE_ROUTER, PUBLIC_ROUTER } from "./router";
function App() {
  const renderElement = (element) => {
    return (
      <Route key={element.key} path={element.path} element={element.element}>
        {element.children
          ? element.children.map((el) => renderElement(el))
          : null}
      </Route>
    );
  };

  return (
    <Routes>
      <Route path="/" element={<BaseLayout />}>
        {PUBLIC_ROUTER.map((el) => renderElement(el))}
        {BASE_ROUTER.map(el=><Route key={el.key} path={el.path} element={el.element}/>)}
      </Route>
      <Route path="*" element={<NotFound />} />
    </Routes>
  );
}

export default App;
