export type Kebab<T extends string, A extends string = ""> = T extends `${infer F}${infer R}` ? Kebab<R, `${A}${F extends Lowercase<F> ? "" : "-"}${Lowercase<F>}`> : A;
declare function camelToKebab<T extends string>(string: T): Kebab<T>;
declare function arrayify<T = unknown>(obj: T): (T & any[]) | T[];
declare function nullify<T = unknown>(value: T): NonNullable<T> | null;
export { camelToKebab, nullify, arrayify };
