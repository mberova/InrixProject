/**  */
export type List<A> =
    | "nil"
    | {readonly kind: "cons", readonly hd: A, readonly tl: List<A>};


/** The empty list. */
export const nil: "nil" = "nil";

/** Returns a list with hd in front of tl. */
export const cons = <A,>(hd: A, tl: List<A>): List<A> => {
  return {kind: "cons", hd: hd, tl: tl};
};