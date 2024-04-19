class RayAnchor
{
    constructor(x, y)
    {
        this.pos = createVector(x, y);
    }

    display()
    {
        fill(180);
        noStroke();
        circle(this.pos.x, this.pos.y, 8);
    }
}