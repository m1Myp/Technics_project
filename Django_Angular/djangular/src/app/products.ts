export interface Product {
  name: string,
  manufacturer: string,
  price: number,
  picture: string
}

export interface ProductArray extends Array<Product> { }
