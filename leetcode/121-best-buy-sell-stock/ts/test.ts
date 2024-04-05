import { expect } from "chai";
import "mocha";
import { maxProfit } from "./solution";

describe.skip("Best time to buy and sell stock", () => {
    it("should return highest profit when it's possible to make a profit", () => {
        const stockPrices:Array<number> = [7,1,5,3,6,4];
        const expectedProfit = 5; //buy on day 2 (1) and sell on day 5 (6) => 6 - 1 = 5

        const profit:number = maxProfit(stockPrices);

        expect(profit).to.be.equal(expectedProfit);
    });

    it("should return zero profit when it's impossible to make a profit", () => {
        const stockPrices:Array<number> = [7,6,4,3,1];
        const expectedProfit = 0;

        const profit:number = maxProfit(stockPrices);

        expect(profit).to.be.equal(expectedProfit);
    });

    it("should return zero profit when considering a single day", () => {
        const stockPrices:Array<number> = [7];
        const expectedProfit = 0;

        const profit:number = maxProfit(stockPrices);

        expect(profit).to.be.equal(expectedProfit);
    });
});