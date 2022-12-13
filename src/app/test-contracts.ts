export interface Info {
  product_ID: string,
  product_name: string,
  product_manufacturer: string,
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
