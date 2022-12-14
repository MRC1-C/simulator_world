import { useNavigate } from "react-router-dom";
import Product from "./product.json";

const ProductComponent = ({ name1, name2, url_img }) => {
  const navigate = useNavigate();
  return (
    <div
      className="p-4 w-full shadow-xl shadow-primary rounded-lg transition ease-in-out delay-100 hover:scale-105 bg-white cursor-pointer"
      onClick={() => navigate("/blog/" + name1)}
    >
      <div className="p-4">
        <img
          src={url_img}
          alt="product"
          className="w-full h-[246px] rounded-lg object-cover"
        />
        <div className="flex justify-between pt-3">
          <div>
            <p className="text-[18px] text-[#111029] pt-3">{name1}</p>
            <p className="text-[18px] text-[#111029] font-light">{name2}</p>
          </div>
          <img src="/logo.png" className="object-contain" width={26} />
        </div>
      </div>
    </div>
  );
};

function Blog() {
  return (
    <div>
      <div className="grid grid-cols-1 md:grid-cols-6 gap-10">
        {/* <div className="col-span-1"></div> */}
        <div className="col-span-6 p-4 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-3 gap-7">
          {Product.map((pr) => (
            <ProductComponent {...pr} />
          ))}
        </div>
        {/* <div className="col-span-1"></div> */}
      </div>
    </div>
  );
}

export default Blog;
