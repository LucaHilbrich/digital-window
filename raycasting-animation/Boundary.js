class Boundary
{
    constructor(x1, y1, x2, y2)
    {
        this.x1 = x1;
        this.y1 = y1;
        this.x2 = x2;
        this.y2 = y2;
        this.intersection = false;
    }

    is_intersecting(x3, y3, x4, y4)
    {
        let x12 = this.x1 - this.x2;
        let x34 = x3 - x4;
        let y12 = this.y1 - this.y2;
        let y34 = y3 - y4;

        let c = x12 * y34 - y12 * x34;

        if (abs(c) < 0.01)
        {
            // no intersection
            return false;
        }
        else
        {
            // intersection
            let a = this.x1 * this.y2 - this.y1 * this.x2;
            let b = x3 * y4 - y3 * x4;

            this.intersection = createVector(
                (a * x34 - b * x12) / c,
                (a * y34 - b * y12) / c
            );

            let bbox_max_x = max(this.x1, this.x2);
            let bbox_min_x = min(this.x1, this.x2);
            let bbox_max_y = max(this.y1, this.y2);
            let bbox_min_y = min(this.y1, this.y2);
            if (this.intersection.x >= bbox_min_x && this.intersection.x < bbox_max_x &&
                this.intersection.y >= bbox_min_y && this.intersection.y < bbox_max_y)
            {
                return true;
            }
            return false;
        }
    }

    display()
    {
        noFill();
        stroke(180);
        line(this.x1, this.y1, this.x2, this.y2);
    }
}