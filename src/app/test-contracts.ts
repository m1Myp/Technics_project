export interface Info {
  product_ID: string,
  product_name: string,
  product_manufacturer: string,
  product_category_ID: string,
  product_characteristics: string,
  pictures: PicturesArray;
  urls: UrlArray;
}
export interface InfoArray extends Array<Info> { }

export interface Pictures {
    picture_URL: string;
}
export interface PicturesArray extends Array<Pictures> { }

export interface Url {
  cost: Cost;
  product_URL: string;
  product_shop: string;
}
export interface UrlArray extends Array<Url> { }

export interface Cost {
  product_cost: number;
}

export interface Category {
  category_name: string;
}

export interface PageResponse {
  products: InfoArray;
  total_count_products: number;
}